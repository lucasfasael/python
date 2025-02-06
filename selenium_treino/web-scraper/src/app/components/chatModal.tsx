import { useState} from 'react';
import { PaperAirplaneIcon, XMarkIcon, ArrowPathIcon } from '@heroicons/react/24/outline';

type Message = {
  text: string;
  isBot: boolean;
  timestamp: Date;
};

const ChatModal = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showModal, setShowModal] = useState(true);

  const handleSendMessage = async () => {
    if (!inputText.trim()) return;

    // Adiciona mensagem do usuário
    setMessages(prev => [...prev, {
      text: inputText,
      isBot: false,
      timestamp: new Date()
    }]);

    // Simula resposta do bot
    setIsLoading(true);
    setInputText('');

    setTimeout(() => {
      setMessages(prev => [...prev, {
        text: 'Isso é uma resposta simulada do bot!',
        isBot: true,
        timestamp: new Date()
      }]);
      setIsLoading(false);
    }, 1500);
  };

  if (!showModal) return null;

  return (
    <div className="fixed bottom-8 right-8 z-50">
      <div className="bg-white rounded-2xl shadow-xl w-96 h-[600px] flex flex-col">
        {/* Header */}
        <div className="bg-blue-600 text-white p-4 rounded-t-2xl flex justify-between items-center">
          <div className="flex items-center gap-3">
            <div className="bg-white/20 p-2 rounded-full">
              🤖
            </div>
            <h2 className="text-lg font-semibold">ChatBot Assistente</h2>
          </div>
          <button
            onClick={() => setShowModal(false)}
            className="hover:bg-white/10 p-1 rounded-full"
          >
            <XMarkIcon className="w-6 h-6" />
          </button>
        </div>

        {/* Área de Mensagens */}
        <div className="flex-1 p-4 overflow-y-auto space-y-4">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`flex ${message.isBot ? 'justify-start' : 'justify-end'}`}
            >
              <div
                className={`max-w-[80%] p-3 rounded-2xl ${
                  message.isBot
                    ? 'bg-gray-100 text-black'
                    : 'bg-blue-600 text-white'
                }`}
              >
                <p className="text-sm">{message.text}</p>
                <p className="text-xs mt-1 opacity-70">
                  {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </p>
              </div>
            </div>
          ))}

          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-gray-100 p-3 rounded-2xl">
                <ArrowPathIcon className="w-5 h-5 animate-spin" />
              </div>
            </div>
          )}
        </div>

        {/* Input Area */}
        <div className="p-4 border-t">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleSendMessage();
            }}
            className="flex gap-2"
          >
            <input
              type="text"
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              placeholder="Digite sua mensagem..."
              className="flex-1 p-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
              disabled={isLoading}
              autoFocus
            />
            <button
              type="submit"
              className="bg-blue-600 text-white p-2 rounded-xl hover:bg-blue-700 disabled:opacity-50"
              disabled={!inputText.trim() || isLoading}
            >
              <PaperAirplaneIcon className="w-5 h-5" />
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default ChatModal;