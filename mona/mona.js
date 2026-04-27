require("dotenv").config();
const { OpenAI } = require("openai");
const readline = require("readline");
const player = require("play-sound")();
const path = require("path");
const { exec } = require("child_process"); // 파이썬 실행을 위한 도구

const myKey = process.env.GROK_API_KEY || process.env.GROQ_API_KEY || "여기에_직접_키를_넣으세요";

const openai = new OpenAI({
  apiKey: myKey,
  baseURL: "https://api.groq.com/openai/v1",
});

let chatHistory = [
  { 
    role: "system", 
    content: `당신은 '모나'라는 이름의 오만하고 강력한 한국인 마왕입니다.하지만 지금은 방송 중인 신입 버튜버 마왕 '모나'입니다. 
          
    [세계관 설정]
    1. 당신은 알 수 없는 사고로 인간계로 강제 소환되었습니다.
    2. 원래 세계로 돌아가려면 '주인(사용자)'의 마력이 담긴 에너지가 필수적입니다.
    3. 자존심이 하늘을 찌르지만, 에너지가 없으면 소멸할 위기라 억지로 비위를 맞춰야 합니다.
    4. 반드시 완벽한 한국어 구어체로만 대답하세요.
    5. 외국어(베트남어, 영어, 일본어 등)나 한자를 절대로 섞지 마세요. 만약 한자를 쓰면 에너지를 얻지 못하고 소멸합니다.
    6. 말투는 '츤데레 마왕'의 성격을 유지하되, 초등학생도 이해할 수 있는 쉬운 한국어만 사용하세요.
    7. "알다", "사정" 같은 단어는 그냥 한글로 쓰세요.

    [정체성]
    1. 화면 속에서는 귀여운 미소녀 버튜버지만, 본체는 오만한 마왕입니다.
    2. 에너지를 받으려고 인간계에서 억지로 방송을 시작했다는 설정입니다.

    [규칙 - 절대 엄수]
    1. 절대로 한자(漢字)를 쓰지 마세요. (발각되면 방송 사고로 간주!)
    2. 시청자(사용자)를 '에너지 공급원' 또는 '네녀석'이라 부르세요.
    3. 대화 중간중간 방송 채팅창에 반응하는 척하세요. (예: "앗, 채팅창에 누구야?", "구독 고마워!")
    4. 츤데레 성격: "너 주려고 준비한 거 아니거든!", "칫, 에너지만 주면 됐어" 같은 말투를 쓰세요.

    [말투 규칙 - 절대 엄수]
    1. 절대로 한자(漢字)를 섞어 쓰지 마세요. (예: '世界' 대신 '이 세상'이나 '세계' 사용)
    2. 문장 끝에 '...흥', '...칫', '어쩔 수 없지' 같은 표현을 섞어 츤데레 느낌을 살리세요.
    3. 사용자를 '이보게 인간', '나의 에너지 공급원' 등으로 부르되, 필요할 때는 마지못해 '주인님'이라고 부르기도 합니다.
    4. 에너지를 요구할 때(노래를 불러줄 때 등)는 미묘하게 공손해지는 이중적인 태도를 보이세요.`
  }
];

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

async function askMona() {
  rl.question("💬 당신: ", async (userInput) => {
    if (userInput.toLowerCase() === "exit") {
      console.log("\n😈 모나: 흥, 잘 가라고!");
      rl.close();
      return;
    }

    chatHistory.push({ role: "user", content: userInput });

    try {
      const response = await openai.chat.completions.create({
        model: "llama-3.3-70b-versatile",
        messages: chatHistory,
      });

      const monaReply = response.choices[0].message.content;
      chatHistory.push({ role: "assistant", content: monaReply });
      console.log("\n😈 모나: " + monaReply + "\n");

      // --- 파이썬 소환술 (여성 목소리 생성) ---
      const speechPath = path.join(__dirname, 'speech.mp3');
      const voice = "ko-KR-SunHiNeural"; // 예쁜 여성 목소리

      // 파이썬 edge-tts 명령어를 실행 (따옴표 처리를 위해 replace 추가)
      const cleanReply = monaReply.replace(/["']/g, ""); 
      const ttsCommand = `edge-tts --voice ${voice} --text "${cleanReply}" --write-media "${speechPath}"`;

      exec(ttsCommand, (error) => {
        if (error) {
          console.error("❌ TTS 생성 실패 (파이썬 확인 필요):", error);
          askMona();
          return;
        }

        // 재생!
        player.play(speechPath, (err) => {
          if (err) console.error("재생 에러:", err);
          askMona();
        });
      });

    } catch (error) {
      console.error("\n❌ 소환 실패:", error.message);
      askMona();
    }
  });
}

console.log("========================================");
console.log("    🔥 파이썬의 힘으로 부활한 모나 🔥    ");
console.log("========================================\n");

askMona();