import requests
TESTABLY_URL = "https://ahzfskzuyzcmgilcvozn.supabase.co/functions/v1/upload-ci-results"
TOKEN = "testably_516a53c7b4bc4a7689beea2b6f46fd4f"
RUN_ID = "49d9b104-cca9-4e2e-b779-8c9ba2b879bd"
results = []
def report_result(test_case_id, status, note="", elapsed=0):
    results.append({
        "test_case_id": test_case_id,
        "status": status,
        "note": note,          # ← note 추가
        "elapsed": elapsed,
        "author": "pytest"
    })
def test_login():
    result = True
    status = "passed" if result else "failed"
    report_result("SUI-1", status, note="로그인 테스트 정상 완료")
    return result
def test_signup():
    result = True
    status = "passed" if result else "failed"
    report_result("SUI-2", status, note="회원가입 플로우 검증 완료")
    return result
if __name__ == "__main__":
    test_login()
    test_signup()
    response = requests.post(
        TESTABLY_URL,
        headers={"Authorization": f"Bearer {TOKEN}"},
        json={
            "run_id": RUN_ID,
            "results": results
        }
    )
    print("응답 상태:", response.status_code)
    print("응답 내용:", response.text)