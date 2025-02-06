const VideoButton = () => {
  return (
    <div
      className="
        absolute 
        bottom-6 
        right-6 
        flex w-28 
        cursor-pointer 
        flex-col 
        items-center 
        rounded-full 
        shadow-lg 
        transition-transform 
        duration-300 
        hover:scale-125 
        
        "
    >
      {/* Balão de fala */}
      <div
        className="
          relative 
          mb-2 
          rounded-lg 
          bg-gray-200 
          px-3 
          py-1 
          text-sm 
          font-medium 
          text-black 
          shadow-md
      "
      >
        Como posso ajudar?
        <div
          className="
                absolute 
                -bottom-2 
                left /* Posiciona mais para a esquerda */
                h-0 
                w-0 
                border-l-[10px] 
                border-r-[10px] 
                border-t-[12px] 
                border-l-transparent 
                border-r-transparent 
                border-t-gray-200
        "
        ></div>
      </div>

      {/* Vídeo dentro da div pai */}
      <div
        className="
          h-28 
          w-28 
          overflow-hidden 
          rounded-full
          hover:brightness-200
          border-2
      "
      >
        <video
          autoPlay
          loop
          muted
          playsInline
          className="
            h-full 
            w-full 
            rounded-full 
            object-cover
          "
        >
          <source src="/spellcaster.mp4" type="video/mp4" />
          Seu navegador não suporta vídeos.
        </video>
      </div>
    </div>
  );
};

export default VideoButton;
