// API backend
const API_BASE = "http://127.0.0.1:5000/api/vision";

// DOM
const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");
const imageInput = document.getElementById("imageInput");

// Thêm tin nhắn
function addMessage(text, sender = "ai") {
    const div = document.createElement("div");
    div.className = `chat ${sender}`;
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// AI đang nghĩ
function addThinking() {
    const div = document.createElement("div");
    div.className = "chat ai thinking";
    div.innerText = "🤖 AI đang phân tích...";
    chatBox.appendChild(div);
}

// Xoá thinking
function removeThinking() {
    const t = chatBox.querySelector(".thinking");
    if (t) t.remove();
}

// Gửi chat
async function sendChat(message, imageFile) {
    addThinking();

    const formData = new FormData();
    if (message) formData.append("message", message);
    if (imageFile) formData.append("image", imageFile);

    try {
        const res = await fetch(`${API_BASE}/chat`, {
            method: "POST",
            body: formData
        });

        const data = await res.json();
        removeThinking();
        addMessage(data.reply || "AI không trả lời được.", "ai");

    } catch (err) {
        removeThinking();
        addMessage("❌ Lỗi kết nối AI.", "ai");
        console.error("CHAT ERROR:", err);
    }
}

// Click gửi
function sendMessage() {
    const msg = userInput.value.trim();
    const img = imageInput.files[0] || null;

    if (!msg && !img) return;

    if (msg) addMessage(msg, "user");

    sendChat(msg, img);

    userInput.value = "";
    imageInput.value = null;
}

// Enter gửi
userInput.addEventListener("keydown", e => {
    if (e.key === "Enter") sendMessage();
});
