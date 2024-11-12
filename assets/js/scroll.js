document.addEventListener("DOMContentLoaded", function () {
    const questions = document.querySelectorAll(".single-question");
  
    const showOnScroll = () => {
      const scrollPosition = window.innerHeight + window.scrollY;
  
      questions.forEach((question) => {
        if (scrollPosition > question.offsetTop + 50) {
          question.classList.add("show");
        }
      });
    };
  
    window.addEventListener("scroll", showOnScroll);
  });
  