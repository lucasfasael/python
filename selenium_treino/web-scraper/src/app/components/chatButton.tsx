import Image from 'next/image'

const ChatButton = () => {
  return (
    <div className="absolute bottom-4 right-4 flex h-28 w-28 flex-shrink-0 cursor-pointer items-center justify-center rounded-full bg-black/50 shadow-lg hover:h-40 hover:w-40">
      <Image
        src="/iaGirl.jpeg"
        alt="Chat"
        fill
        className="rounded-full object-cover object-top"
      />
    </div>
  )
}

export default ChatButton
