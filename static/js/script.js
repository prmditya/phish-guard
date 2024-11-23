const loadingElement = document.getElementById('loading');
const alertElement = document.querySelector('.alert');
const resultElement = document.getElementById('result');

document.getElementById('urlForm').addEventListener('submit', function (e) {
  e.preventDefault();
  const url = document.getElementById('url').value;

  // Show the loader
  loadingElement.style.display = 'block';
  alertElement.classList.add('hidden');

  fetch('/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Hide the loader
      loadingElement.style.display = 'none';

      resultElement.innerText = `That link is identified as ${data.result}`;
      // Handle the result
      resultElement.innerText = `That link is identified as ${data.result}`;
      if (data.result === 'Safe') {
        alertElement.classList.remove('hidden', 'result-warning');
        alertElement.classList.add('result-safe');
      } else if (data.result === 'Phishing') {
        alertElement.classList.remove('hidden', 'result-safe');
        alertElement.classList.add('result-warning');
      }
    })
    .catch((error) => {
      // Hide the loader
      loadingElement.style.display = 'none';

      // Show the error
      alertElement.classList.remove('hidden', 'result-safe');
      alertElement.classList.add('result-warning');
      console.error('Error:', error);
      resultElement.innerText = 'An error occurred. Please try again.';
    });
});
