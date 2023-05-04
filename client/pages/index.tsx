import MessageDisplay from "@/components/MessageDisplay";
import Head from "next/head";
import { useState } from "react";

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [disableInput, setDisableInput] = useState(false);

  const detectEnter = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      submit();
    }
  };

  const submit = () => {
    if (input === "" || disableInput) return;
    setDisableInput(true);
    const userMsg: Message = { text: input, type: "user" };
    setMessages([...messages, userMsg]);
    queryServer(userMsg);
    setInput("");
  };

  const queryServer = async (userMsg: Message) => {
    try {
      const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        body: JSON.stringify({ query: userMsg.text }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      if (response.status !== 200) {
        setMessages([
          ...messages,
          userMsg,
          { text: await response.text(), type: "system" },
        ]);
        return;
      }
      const { answer } = await response.json();
      setMessages([...messages, userMsg, { text: answer, type: "bot" }]);
    } catch (error) {
      setMessages([
        ...messages,
        userMsg,
        { text: String(error), type: "system" },
      ]);
    }
    setDisableInput(false);
  };

  return (
    <>
      <Head>
        <title>UTD Admissions Chatbot</title>
        <meta name="description" content="Chatbot for UTD Admissions" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className="flex flex-col h-screen">
        {/* Header */}
        <h1 className="text-4xl font-bold text-center h-10 p-2 fixed top-0 left-0 w-full bg-white">
          UTD Admissions Chatbot
        </h1>
        <div className="h-10 shrink-0"></div>

        {/* Body */}
        <div className="flex-grow overflow-y-scroll">
          {messages.map((message, index) => (
            <MessageDisplay key={index} message={message} />
          ))}
        </div>
        <div className="h-14 w-full shrink-0"></div> {/* Footer Spacer */}

        {/* Footer for Text Input */}
        <div className="w-full p-2 fixed bottom-0 left-0 h-14 flex">
          <input
            type="text"
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={detectEnter}
            value={input}
            className="border-2 border-gray-200 text-2xl flex-grow bg-white"
          />
          <button
            className="ml-4 border-2  px-4 border-gray-200 duration-200 hover:bg-slate-200"
            onClick={submit}
          >
            Submit
          </button>
        </div>
      </div>
    </>
  );
}
