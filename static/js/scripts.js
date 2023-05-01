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
  outfitPreview.src = `path/to/${top}_${bottom}.jpg`;
  
  });
  
  // Populate the "Choose a top" dropdown menu
  fetch('/get_tops')
  .then(response => response.json())
  .then(data => {
  const select = document.getElementById('top');
  data.forEach(item => {
  const option = document.createElement('option');
  option.text = item.name;
  option.value = item.id;
  select.appendChild(option);
  });
  });
  
  // Populate the "Choose a bottom" dropdown menu
  fetch('/get_bottoms')
  .then(response => response.json())
  .then(data => {
  const select = document.getElementById('bottom');
  data.forEach(item => {
  const option = document.createElement('option');
  option.text = item.name;
  option.value = item.id;
  select.appendChild(option);
  });
  });
  
  // Populate the "Choose an accessory" dropdown menu
  fetch('/get_accessories')
  .then(response => response.json())
  .then(data => {
  const select = document.getElementById('accessory');
  data.forEach(item => {
  const option = document.createElement('option');
  option.text = item.name;
  option.value = item.id;
  select.appendChild(option);
  });
  });
  
  // Get the featured products section
  const featuredProducts = document.querySelector('.featured-products');
  
  // Fetch products from database
  fetch('/get_products')
  .then(response => response.json())
  .then(data => {
  // Shuffle the products array
  shuffleArray(data);
  
  javascript
  
    // Create a product card for each item in the array
    data.forEach(item => {
      const productCard = document.createElement('div');
      productCard.classList.add('product-card');
  
      const productImage = document.createElement('img');
      productImage.src = item.image;
      productImage.alt = item.name;
      productCard.appendChild(productImage);
  
      const productName = document.createElement('h3');
      productName.textContent = item.name;
      productCard.appendChild(productName);
  
      const productDescription = document.createElement('p');
      productDescription.textContent = item.description;
      productCard.appendChild(productDescription);
  
      const buyButton = document.createElement('a');
      buyButton.href = '#';
      buyButton.classList.add('cta-button');
      buyButton.textContent = 'Buy Now';
      productCard.appendChild(buyButton);
  
      featuredProducts.appendChild(productCard);
    });
  });
});