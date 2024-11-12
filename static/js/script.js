const alertElement = document.querySelector('.alert');
document.getElementById('urlForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const url = document.getElementById('url').value;

  fetch('/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({url}),
  })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById('result').innerText =
            `That link is identified as ${data.result}`;
        console.log(data.result);
        if (data.result === 'Safe') {
          alertElement.classList.remove('hidden', 'result-warning');
          alertElement.classList.add('result-safe');
        } else if (data.result === 'Phishing') {
          alertElement.classList.remove('hidden', 'result-safe');
          alertElement.classList.add('result-warning');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'An error occurred.';
      });
});