// Switch between login and signup forms
document.getElementById('signup-link').addEventListener('click', function() {
  document.getElementById('login-form').style.display = 'none';
  document.getElementById('signup-form').style.display = 'block';
});

document.getElementById('login-link').addEventListener('click', function() {
  document.getElementById('signup-form').style.display = 'none';
  document.getElementById('login-form').style.display = 'block';
});
