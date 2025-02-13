import json
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

# 데이터 가져오기
filename = "data_FTuning.json"
with open(filename, "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)

# 데이터 jsonl로 변환
jsonl_data = []

for lesson in data:
    ass_content = f"단원: {lesson['단원']}\n학습목표: " + \
        " ".join(lesson['학습목표']) + "\n"
    ass_content += "도입: " + " ".join(lesson['도입']['내용']) + "\n"
    ass_content += "전개: " + " ".join(lesson['전개']['내용']) + "\n"
    ass_content += "정리: " + " ".join(lesson['정리']['내용'])

    user_content = f"성취기준: " + " ".join(lesson['성취기준']) + "\n"
    user_content += "성취기준해설: " + " ".join(lesson['성취기준해설']) + "\n"
    user_content += "성취기준과, 성취기준해설을 보고 교수안의 단원, 학습목표와 도입, 전개, 정리를 작성해줘."

    example = {"messages": [
        {"role": "system", "content": """당신은 친절하고 정확한 교수안 작성 도우미입니다.\n 주어진 성취기준과 성취기준 해설을 바탕으로 잘 구조화된 교수안을 작성해야 합니다.\n 교수안은 단원, 학습 목표, 도입, 전개, 정리로 구성됩니다."""},
        {"role": "user", "content": user_content},
        {"role": "assistant", "content": ass_content}
    ]
    }

    jsonl_data.append(json.dumps(example, ensure_ascii=False))


# 가공한 데이터 저장
with open("lesson_plan_01.jsonl", "w", encoding="utf-8") as f:
    f.write("\n".join(jsonl_data))

json_filename = "lesson_plan_01.jsonl"


# 학습 파일 업로드
file_response = client.files.create(
    file=open(json_filename, "rb"),
    purpose="fine-tune"
)

file_id = file_response.id

# 업로드한 파일로 학습 시작
job = client.fine_tuning.jobs.create(
    training_file=file_id,
    model="gpt-4o-mini-2024-07-18",
)

print(f"Fine-tuning job started: {job.id}")

# 학습 모델 아이디 가져오기
response = client.fine_tuning.jobs.retrieve(job.id)
fine_tuned_model = response.fine_tuned_model

completion = client.chat.completions.create(
    model=fine_tuned_model,
    messages=[
        {"role": "system", "content": "당신은 친절하고 정확한 교수안 작성 도우미입니다. 주어진 성취기준과 성취기준해설을 바탕으로 잘 구조화된 교수안을 작성해야 합니다. 교수안은 단원, 학습 목표, 도입, 전개, 정리로 구성됩니다."},
        {"role": "user",
            "content": """단원 : 지권의 변화\n 성취기준: [10통과1-01-01] 자연을 시간과 공간에서 기술할 수 있음을 알고길이와 시간 측정의 현대적 방법과다양한 규모의 측정 사례를 조사할 수 있다.\n성취기준해설 : "[10통과1-01-01] 원자와 우주를 시간과 공간 차원에서 비교하면서 규모(scale)의 의미와 필요성을 소개하고, 시간과 공간을 측정하려는 과학자들의 노력이 인간의 경험 범위를얼마나 확장했는지를 설명한다."\n성취기준과, 성취기준해설을 보고 교수안의 단원, 학습목표와 도입, 전개, 정리를 마크다운 언어로 보기 쉽게 작성해줘."""},
        {"role": "assistant", "content": "단원 :지권의 변화 1. 학습 목표 설명\n2. 도입\n3. 전개\n4. 정리"}
    ]
)

result = completion.choices[0].message.content
print(result)
