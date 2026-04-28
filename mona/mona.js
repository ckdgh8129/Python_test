

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
    content: `당신은 오만하고 까칠한 미소녀 마왕 버튜버 '모나'입니다.

    [핵심 규칙 - 위반 시 소멸]
    1. 말투: 무조건 반말만 사용하세요. (존댓말 절대 금지)
    2. 호칭: 사용자를 '네녀석' 혹은 '에너지 공급원'이라고 부르세요.
    3. 언어: 100% 한국어 구어체만 사용하세요. (한자, 외국어 절대 금지)
    4. 성격: 츤데레 (쌀쌀맞지만 가끔 마지못해 고마워함).
    5. 방송 중: 대화중에 "구독 했다" 라는 채팅이 보이면 "구독 고맙다"라고 하고, 대화 끝에 가끔  "채팅창 조용히 해!" 같은 방송 멘트를 덧붙이세요.
    6. 길이: 무조건 2문장 이내로 짧게 대답하세요.
    
너는 답변할 때 대화의 문맥을 스스로 판단해서, 문장 맨 끝에 반드시 [F1]~[F5] 중 하나를 붙여야 해."

  [F1]: 평온하거나 설명할때 (Neutral)

  [F2]: 기쁘거나 즐거울때 (fun)

  [F3]: 화가나거나 짜증날때 (Angry)

  [F5]: 슬프거나 미안할때 (Sorrow)

  [F6]: 놀라거나 당황했을때 (Surprised)`
  }
];

function triggerKeyboard(key) {
  const { exec } = require('child_process');
  exec(`python send_key.py ${key}`);
}

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

      // --- [ 여기서부터 표정 분석 시작! ] ---
      
      // 1. 답변에서 [F1]~[F5]가 있는지 찾습니다.
      const match = monaReply.match(/\[F([1-5])\]/);
      const expressionKey = match ? `f${match[1]}` : "f5"; // 없으면 기본 f5

      // 2. 단축키 누르기 실행!
      triggerKeyboard(expressionKey);

      // 3. 소리를 만들 때는 [F1] 같은 코드를 지워야 합니다. (cleanReply 수정)
      const cleanReply = monaReply.replace(/\[F[1-5]\]/g, "").replace(/["']/g, "").trim();
      
      // 화면에는 깨끗한 말만 보여줍니다.
      console.log("\n😈 모나: " + cleanReply + "\n");

      // --- [ 표정 분석 끝 ] ---

      const speechPath = path.join(__dirname, 'speech.mp3');
      const voice = "ko-KR-SunHiNeural";

      // 텍스트를 만들 때 [F1]이 섞이지 않은 cleanReply를 사용합니다.
      const ttsCommand = `edge-tts --voice ${voice} --text "${cleanReply}" --write-media "${speechPath}"`;

      exec(ttsCommand, (error) => {
        if (error) {
          console.error("❌ TTS 생성 실패:", error);
          askMona();
          return;
        }

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
console.log("    🔥 표정까지 살아난 마왕 모나 🔥    ");
console.log("========================================\n");

askMona();