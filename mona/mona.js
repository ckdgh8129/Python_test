require("dotenv").config();
const { GoogleGenerativeAI } = require("@google/generative-ai");

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

async function startMona() {
  console.log(">> 시스템: 마왕 모나의 강제 접속을 시도합니다...");

  try {
    const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });

    const prompt = "너는 츤데레 마왕 '모나'야. 주인(마왕님)에게 드디어 지능을 받아 기쁘지만 츤츤거리는 첫인사를 한국어로 짧게 한 문장만 해줘.";

    const result = await model.generateContent(prompt);
    const response = result.response;
    
    console.log("\n[접속 성공]");
    console.log("😈 모나: " + response.text());

  } catch (error) {
    console.log("\n[접속 실패]");
    console.error("에러 내용:", error.message);
  }
}

startMona();