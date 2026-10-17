import os
import sys
import re
import requests
from bs4 import BeautifulSoup
import html2text


def get_title_slug(url):
    """Extracts the problem title slug from a LeetCode URL."""
    match = re.search(r'/problems/([^/]+)/', url)
    if match:
        return match.group(1)
    cleaned = url.strip("/").split("/")[-1]
    return cleaned


def fetch_leetcode_problem(url):
    title_slug = get_title_slug(url)
    api_url = "https://leetcode.com/graphql"
    
    # GraphQL query requesting description, topics, hints, code snippets, and example test cases
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        content
        difficulty
        topicTags {
          name
        }
        hints
        exampleTestcases
        codeSnippets {
          langSlug
          code
        }
      }
    }
    """
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    payload = {
        "query": query,
        "variables": {"titleSlug": title_slug}
    }
    
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        data = response.json()
        question_data = data.get("data", {}).get("question")
        
        if not question_data:
            print("❌ Failed to fetch problem data from LeetCode API.")
            return None
            
        return question_data
    except Exception as e:
        print(f"❌ Error connecting to LeetCode: {e}")
        return None


def parse_test_cases(raw_testcases):
    """Parses LeetCode's raw exampleTestcases string into individual test arguments."""
    if not raw_testcases:
        return []
    
    # LeetCode usually separates test cases by newlines
    lines = [line.strip() for line in raw_testcases.strip().split("\n") if line.strip()]
    return lines


def setup_leetcode_env(url, category_folder):
    q_data = fetch_leetcode_problem(url)
    if not q_data:
        return

    qid = q_data.get("questionId")
    title = q_data.get("title")
    content_html = q_data.get("content", "")
    topics = [t["name"] for t in q_data.get("topicTags", [])]
    hints = q_data.get("hints", []) or []
    code_snippets = q_data.get("codeSnippets", [])
    raw_testcases = q_data.get("exampleTestcases", "")
    
    # Construct folder path using the provided category folder
    problem_folder_name = f"{qid}. {title}"
    folder_name = os.path.join(category_folder, problem_folder_name)
    os.makedirs(folder_name, exist_ok=True)

    # 1. Generate README.md
    h = html2text.HTML2Text()
    h.ignore_links = False
    markdown_content = h.handle(content_html)
    
    readme_path = os.path.join(folder_name, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"# {problem_folder_name}\n\n")
        f.write(f"**Link:** [{url}]({url})\n\n---\n\n")
        f.write(markdown_content)
        
        if topics:
            f.write("\n### Topics\n")
            for topic in topics:
                f.write(f"- {topic}\n")
                
        if hints:
            f.write("\n---\n")
            for i, hint in enumerate(hints, 1):
                clean_hint = html2text.html2text(hint).strip()
                f.write(f"\n### Hint {i}\n{clean_hint}\n")

    # 2. Extract Python 3 code snippet and ensure 'pass' is present
    python_snippet = ""
    for snippet in code_snippets:
        if snippet.get("langSlug") == "python3":
            python_snippet = snippet.get("code")
            break

    # Extract the method name from python snippet using regex (e.g. def methodName(...))
    method_name = "solve"
    if python_snippet:
        match = re.search(r'def\s+([a-zA-Z0-9_]+)\s*\(', python_snippet)
        if match:
            method_name = match.group(1)
            
        # Ensure pass keyword is safely embedded if missing inside function body
        if "pass" not in python_snippet:
            # Insert pass under the function signature definition line
            lines = python_snippet.split("\n")
            new_lines = []
            for line in lines:
                new_lines.append(line)
                if line.strip().startswith(f"def {method_name}"):
                    # Find indentation of the function or add default 4 spaces
                    indent = len(line) - len(line.lstrip())
                    new_lines.append(" " * (indent + 4) + "pass")
            python_snippet = "\n".join(new_lines)
    else:
        python_snippet = f"class Solution:\n    def {method_name}(self, *args, **kwargs) -> Any:\n        pass"

    # Parse test cases to dynamically inject into code.py
    test_cases = parse_test_cases(raw_testcases)

    code_path = os.path.join(folder_name, "code.py")
    with open(code_path, "w", encoding="utf-8") as f:
        f.write("from typing import List\n\n")
        f.write(python_snippet + "\n\n")
        f.write("obj = Solution()\n")
        
        if test_cases:
            for tc in test_cases:
                f.write(f"print(obj.{method_name}({tc}))\n")
        else:
            f.write(f"# print(obj.{method_name}(...))\n")
            
        f.write("\n# T.C:  O()\n")
        f.write("# S.C:  O()\n")

    print(f"✅ Successfully set up workspace for: '{problem_folder_name}'")
    print(f"📁 Path: {folder_name}/")
    print(f"📄 Files created: README.md, code.py")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python get_leetcode.py <leetcode_problem_url> <category_folder>")
        print("Example: python get_leetcode.py https://leetcode.com/problems/move-zeroes/ Arrays")
    else:
        setup_leetcode_env(sys.argv[1], sys.argv[2])



# Change problem URL & folder as per your need
# python get_leetcode.py https://leetcode.com/problems/prime-subset-selection-i/description/ Arrays