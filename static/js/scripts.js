document.addEventListener('DOMContentLoaded', () => {
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    const teamMembers = document.querySelectorAll('.team-member');
  
    let currentIndex = 0;
  
    function setActive(index) {
      teamMembers.forEach(member => member.classList.remove('active'));
      teamMembers[index].classList.add('active');
    }
  
    function updateIndex(step) {
      currentIndex += step;
      if (currentIndex < 0) {
        currentIndex = teamMembers.length - 1;
      } else if (currentIndex >= teamMembers.length) {
        currentIndex = 0;
      }
      setActive(currentIndex);
    }
  
    prevBtn.addEventListener('click', () => updateIndex(-1));
    nextBtn.addEventListener('click', () => updateIndex(1));
  });
  