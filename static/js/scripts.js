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

    
  function updateTopSlideshow(tops) {
    const slideshow = document.querySelector('.slideshow.tops .slideshow-container');
    slideshow.innerHTML = '';
    tops.forEach(top => {
      const slide = document.createElement('div');
      slide.classList.add('slide');
      slide.setAttribute('data-type', top[3]);
      slide.setAttribute('data-size', top[4]);
      slide.setAttribute('data-price', top[5]);
      slide.setAttribute('data-color', top[6]);
      slide.innerHTML = `
        <img src="data:image/jpeg;base64,${top[6]}" alt="${top[2]}">
        <div class="caption">${top[2]} - ${top[3]} - ${top[4]} - ${top[5]}</div>
      `;
      slideshow.appendChild(slide);
    });
  }
    
    function updateBottomSlideshow(bottoms) {
      const slideshow = document.querySelector('.slideshow.bottoms .slideshow-container');
      slideshow.innerHTML = '';
      bottoms.forEach(bottom => {
        const slide = document.createElement('div');
        slide.classList.add('slide');
        slide.setAttribute('data-type', bottom[3]);
        slide.setAttribute('data-size', bottom[4]);
        slide.setAttribute('data-price', bottom[5]);
        slide.setAttribute('data-color', bottom[6]);
        slide.innerHTML = `
          <img src="data:image/jpeg;base64,${bottom[6]}" alt="${bottom[2]}">
          <div class="caption">${bottom[2]} - ${bottom[3]} - ${bottom[4]} - ${bottom[5]}</div>
        `;
        slideshow.appendChild(slide);
      });
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
    
    function register() {
      var username = $('#username').val();
      var password = $('#password').val();
    
      if (username === '' || password === '') {
        alert('Please fill in both fields.');
      } else {
        $.ajax({
          type: 'POST',
          url: '{{ url_for(templates,     filename=/login.html) }}',
          data: {'username': username, 'password': password},
          success: function(data) {
            window.location.href = '{{ url_for(templates,     filename=/login.html) }}';
          },
          error: function(xhr, status, error) {
            alert(xhr.responseText);
          }
        });
      }
    }
    
    function login() {
      var username = $('#username').val();
        var password = $('#password').val();
    
        if (username === '' || password === '') {
          alert('Please fill in both fields.');
        } else {
          $.ajax({
            type: 'POST',
            url: '{{ url_for(templates,     filename=/login.html) }}',
            data: {'username': username, 'password': password},
            success: function(data) {
              if (data === 'success') {
                window.location.href = '{{ url_for(templates,     filename=/user.html) }}';
              } else {
                alert('Incorrect username or password.');
              }
            }
          });
        }
    }
    
    
    function updateSlideshows() {
      const filterData = {
        type: $("#type").val(),
        size: $("#size").val(),
        price: $("#price").val(),
        color: $("#color").val()
      };
    
      $.ajax({
        url: "/filter",
        type: "POST",
        data: filterData,
        success: function(response) {
          updateTopSlideshow(response.tops);
          updateBottomSlideshow(response.bottoms);
        }
      });
    }
    


    // Function to shuffle the array in-place
    function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
    }
    }
      

    // Populate dropdowns with items from database
    const topDropdown = document.getElementById('top');
    const bottomDropdown = document.getElementById('bottom');

    fetch('/tops')
      .then(response => response.json())
      .then(data => {
        data.forEach(top => {
          const option = document.createElement('option');
          option.value = top.id;
          option.text = top.name;
          topDropdown.add(option);
        });
      });

    fetch('/bottoms')
      .then(response => response.json())
      .then(data => {
        data.forEach(bottom => {
          const option = document.createElement('option');
          option.value = bottom.id;
          option.text = bottom.name;
          bottomDropdown.add(option);
        });
      });

    // Handle form submission
    const form = document.getElementById('outfit-form');

    form.addEventListener('submit', event => {
      event.preventDefault();
      
      const formData = new FormData(form);
      
      fetch('/outfits', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        console.log(data); // Log the response from the server
      })
      .catch(error => console.error(error));
    });
}
});
