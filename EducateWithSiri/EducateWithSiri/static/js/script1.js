// JavaScript code to continuously move the text

function startContinuousAnimation() {
    const header = document.querySelector('.move-text');
    header.classList.remove('move-text');
    void header.offsetWidth; // Trigger reflow to restart the animation
    header.classList.add('move-text');
  }
  
  // Start the animation when the page loads
  window.addEventListener('load', function () {
    startContinuousAnimation();
  });
  
  // Optionally, you can also trigger the animation at regular intervals
  setInterval(startContinuousAnimation, 5000); // Restart the animation every 5 seconds
  