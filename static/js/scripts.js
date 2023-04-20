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
  

  // Get the View Resume link for each programmer slide
var resume1 = document.getElementById("resume1");
var resume2 = document.getElementById("resume2");
var resume3 = document.getElementById("resume3");

// Add an event listener to download the correct resume when the link is clicked
resume1.addEventListener("click", function() {
  window.location.href = "{{ url_for('static', filename='img/about/resumes/Resume_Cris.pdf') }}";
});

resume2.addEventListener("click", function() {
  window.location.href = "{{ url_for('static', filename='img/about/resumes/Resume_John.pdf') }}";
});

resume3.addEventListener("click", function() {
  window.location.href = "{{ url_for('static', filename='img/about/resumes/Resume_Evan.pdf') }}";
});
