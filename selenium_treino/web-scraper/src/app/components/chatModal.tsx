interface ChatModalProps {
  onClose: () => void;
}

const ChatModal = ({ onClose }: ChatModalProps) => {
  return (
    <div>
      <h1 onClick={onClose}>TESTE</h1>
    </div>
  );
};

export default ChatModal;
