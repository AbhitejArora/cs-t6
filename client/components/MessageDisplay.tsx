const MessageDisplay = ({ message }: { message: Message }) => {
  if (message.type === "user") {
    return (
      <div className="flex justify-end">
        <div className="bg-blue-500 text-white p-2 rounded-lg m-2">
          {message.text}
        </div>
      </div>
    );
  } else if (message.type === "bot") {
    return (
      <div className="flex justify-start">
        <div className="bg-gray-300 text-black p-2 rounded-lg m-2">
          {message.text}
        </div>
      </div>
    );
  } else {
    return (
      <div className="flex justify-center">
        <div className="bg-red-400 text-white p-2 rounded-lg m-2">
          {message.text}
        </div>
      </div>
    );
  }
};

export default MessageDisplay;
