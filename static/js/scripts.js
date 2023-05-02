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

  const outfitForm = document.querySelector('.outfit form');
  const outfitPreview = document.querySelector('.outfit-preview img');

  outfitForm.addEventListener('submit', event => {
    event.preventDefault();

    // Get selected values from form
    const top = document.querySelector('#top').value;
    const bottom = document.querySelector('#bottom').value;

    // Set outfit preview image source
    outfitPreview.src = `path/to/${top}_${bottom}.png`;
  });



  function createSlideshow(slideshowContainer, products) {
    slideshowContainer.innerHTML = '';
    products.forEach(product => {
        const slide = document.createElement('div');
        slide.className = 'slide';
        slide.innerHTML = `
            <img src="${product[1]}" alt="${product[2]}">
            <div class="caption">${product[2]} - ${product[3]} - ${product[4]} - ${product[5]}</div>
        `;
        slideshowContainer.appendChild(slide);
    });
}

function updateSlideshows(tops, bottoms) {
    const topsSlideshow = document.querySelector('.slideshow-container.tops');
    const bottomsSlideshow = document.querySelector('.slideshow-container.bottoms');
    createSlideshow(topsSlideshow, tops);
    createSlideshow(bottomsSlideshow, bottoms);
}
filterSubmitButton.addEventListener('click', (event) => {
  event.preventDefault();
  const formData = new FormData(filterForm);
  fetch('/filter', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      const filteredTops = data.filter(product => product[2] === 'top');
      const filteredBottoms = data.filter(product => product[2] === 'bottom');
      updateSlideshows(filteredTops, filteredBottoms);
  });
});



    
  // Function to shuffle the array in-place
  function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
  const j = Math.floor(Math.random() * (i + 1));
  [array[i], array[j]] = [array[j], array[i]];
  }
  }
  });