import argparse
import subprocess
from datetime import datetime


def save_trace_log(why: str, what: str, log_file: str = "trace_log.md"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = (
        f"## [{timestamp}]\n"
        f"- **Why (의사결정 배경):** {why}\n"
        f"- **What (작업 내용):** {what}\n\n"
    )
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"[성공] '{log_file}'에 의사결정 로그가 기록되었습니다.")


def git_commit(what: str, log_file: str = "trace_log.md"):
    subprocess.run(["git", "add", log_file], check=True)
    subprocess.run(
        ["git", "commit", "--only", log_file, "-m", f"docs(trace): {what}"],
        check=True,
    )
    print("[성공] Git 커밋이 완료되었습니다.")


def main():
    parser = argparse.ArgumentParser(description="LLM Agent 작업 의사결정(Why-What) 추적 CLI")
    parser.add_argument("--why", required=True, help="작업을 수행하는 이유 및 배경")
    parser.add_argument("--what", required=True, help="수행한 구체적 작업 내용")
    parser.add_argument("--commit", action="store_true", help="로그 기록 후 자동 Git 커밋 실행")
    args = parser.parse_args()

    save_trace_log(args.why, args.what)
    if args.commit:
        git_commit(args.what)


if __name__ == "__main__":
    main()
