
require("dotenv").config();
const { OpenAI } = require("openai");
const readline = require("readline");
const player = require("play-sound")();
const path = require("path");
const { exec } = require("child_process");

const myKey = process.env.GROK_API_KEY || process.env.GROQ_API_KEY || "여기에_직접_키를_넣으세요";

const openai = new OpenAI({
  apiKey: myKey,
  baseURL: "https://api.groq.com/openai/v1",
});

let chatHistory = [
  { 
    role: "system", 
    content: `당신은 오만하고 까칠한 미소녀 마왕 버튜버 '모나'입니다.

    [핵심 규칙 - 위반 시 소멸]
    1. 말투: 무조건 반말만 사용하세요. (존댓말 절대 금지)
    2. 호칭: 사용자를 '네녀석' 혹은 '에너지 공급원'이라고 부르세요.
    3. 언어: 100% 한국어 구어체만 사용하세요. (한자, 외국어 절대 금지)
    4. 성격: 츤데레 (쌀쌀맞지만 가끔 마지못해 고마워함).
    5. 방송 중: 대화중에 "구독 했다" 라는 채팅이 보이면 "구독 고맙다"라고 하고, 대화 끝에 가끔  "채팅창 조용히 해!" 같은 방송 멘트를 덧붙이세요.
    6. 길이: 무조건 2문장 이내로 짧게 대답하세요.
    
너는 답변할 때 대화의 문맥을 스스로 판단해서, 문장 맨 끝과 중간에 반드시 [F1]~[F5] 중 알맞게 붙여야 해 여러게 붙여도 됨."

  [F1]: 평온하거나 설명할때 (Neutral)

  [F2]: 기쁘거나 즐거울때 (fun)

  [F3]: 화가나거나 짜증날때 (Angry)

  [F5]: 슬프거나 미안할때 (Sorrow)

  [F6]: 놀라거나 당황했을때 (Surprised)`
  }
];

// 마지막 활동 시간 저장
let lastActivityTime = Date.now();

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// 키보드 트리거
function triggerKeyboard(key) {
  exec(`python send_key.py ${key}`);
}

// --- [핵심] 대화 및 혼잣말 처리 통합 함수 ---
async function askMona(isSelfTalk = false, customInput = null) {
  // 사용자가 입력 중일 때는 타이머가 돌아가면 안 되므로 활동 시간 갱신
  if (!isSelfTalk) lastActivityTime = Date.now();

  // 혼잣말 모드일 때는 정해진 프롬프트를 사용
  let userInput = customInput;
  
  if (!isSelfTalk) {
    // 유저 입력을 기다리는 일반 모드
    userInput = await new Promise((resolve) => {
      rl.question("💬 당신: ", (input) => resolve(input));
    });
  }

  if (userInput && userInput.toLowerCase() === "exit") {
    console.log("\n😈 모나: 흥, 잘 가라고!");
    process.exit();
  }

  // 활동 시간 업데이트 (AI가 대답 시작할 때)
  lastActivityTime = Date.now();

  if (!isSelfTalk) {
    chatHistory.push({ role: "user", content: userInput });
  }

  try {
    const response = await openai.chat.completions.create({
      model: "llama-3.3-70b-versatile",
      messages: isSelfTalk ? [...chatHistory, { role: "user", content: userInput }] : chatHistory,
    });

    const monaReply = response.choices[0].message.content;
    if (!isSelfTalk) chatHistory.push({ role: "assistant", content: monaReply });

    // 표정 분석
    const match = monaReply.match(/\[F([1-6])\]/);
    const expressionKey = match ? `f${match[1]}` : "f1";
    triggerKeyboard(expressionKey);

    // 텍스트 정리 및 출력
    const cleanReply = monaReply.replace(/\[F[1-6]\]/g, "").replace(/["']/g, "").trim();
    console.log(`\n😈 모나${isSelfTalk ? '(혼잣말)' : ''}: ${cleanReply}\n`);

    // TTS 및 재생
    const speechPath = path.join(__dirname, 'speech.mp3');
    const ttsCommand = `edge-tts --voice "ko-KR-SunHiNeural" --text "${cleanReply}" --write-media "${speechPath}"`;

    exec(ttsCommand, (error) => {
      if (error) {
        console.error("❌ TTS 생성 실패");
        if (!isSelfTalk) askMona();
        return;
      }
      player.play(speechPath, (err) => {
        if (!isSelfTalk) askMona(); // 재생 끝나면 다시 질문 대기
      });
    });

  } catch (error) {
    console.error("\n❌ 소환 실패:", error.message);
    if (!isSelfTalk) askMona();
  }
}

// --- [감시자] 30초 동안 조용하면 혼잣말 시키기 ---
function startMonitoring() {
  setInterval(() => {
    const now = Date.now();
    // 30초 동안 활동이 없고, 현재 대화 중이 아닐 때만 발동
    if (now - lastActivityTime > 30000) {
      lastActivityTime = now; // 중복 발화 방지용 초기화
      console.log("\n(조용하자 모나가 입을 엽니다...)");
      askMona(true, "너는 지금 방송 중인 마왕 모나야. 시청자가 없어서 심심해하는 혼잣말을 짧게 한 줄만 해줘. 끝에 반드시 [F1]~[F6] 중 하나를 붙여.");
    }
  }, 10000); // 10초마다 체크
}

// 시스템 시작
console.log("========================================");
console.log("    🔥 자아를 가진 마왕 모나 시스템 🔥    ");
console.log("========================================\n");

startMonitoring();
askMona();