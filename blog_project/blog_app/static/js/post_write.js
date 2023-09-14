
tinymce.init({
    selector: '#content',
    images_upload_url: '',
});

document.querySelector("#image_input").addEventListener('change', function() {
  let formData = new FormData();
  formData.append('file', this.files[0]);
  const csrfToken = document.querySelector("#uploadform > input[type=hidden]").value

  fetch('http://127.0.0.1:8000/post/write/upload', {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': csrfToken
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // tinyMCE.activeEditor.insertContent(`<img src="${data.location}"/>`);
  })
  .catch(error => {
    console.error('Error:', error)
  });
});
