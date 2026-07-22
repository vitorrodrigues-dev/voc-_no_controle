document.addEventListener("DOMContentLoaded", () => {
    const anel = document.querySelector(".anel-progresso");

    if (anel) {
        const percentualFinal = getComputedStyle(anel).getPropertyValue("--percentual").trim();

        anel.style.setProperty("--percentual", 0);

        requestAnimationFrame(() => {
            setTimeout(() => {
                anel.style.setProperty("--percentual", percentualFinal);
            }, 100);
        });
    }
});