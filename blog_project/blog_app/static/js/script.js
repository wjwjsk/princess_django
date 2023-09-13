
tinymce.init({
selector: '#content',
images_upload_url: '{% url "blog_app:image_upload" %}',
});

document.addEventListener('DOMContentLoaded', (event) => {

// 이미지 업로드 후 에디터 내에 이미지 삽입
document.getElementById('imageUpload').addEventListener('change', function() {
    let formData = new FormData();
    formData.append('file', this.files[0]);

    fetch('{% url "blog_app:image_upload" %}', {
    method: 'POST',
    body: formData,
    headers: {
        'X-CSRFToken': '{{ csrf_token }}'
    }
    })
    .then(response => response.json())
    .then(data => {
    tinyMCE.activeEditor.insertContent(`<img src="${data.location}"/>`);
    })
    .catch(error => console.error('Error:', error));
});

// AI 글 자동완성
document.getElementById('aiAutocompleteButton').addEventListener('click', function() {
    // 로딩 애니메이션 
    document.getElementById('loading-animation').style.display = 'block';
    document.getElementById('ai-img').style.display = 'none';

    let title = document.getElementById('title').value;
    fetch('/autocomplete/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': '{{ csrf_token }}',
    },
    body: new URLSearchParams({
        'title': title
    })
    })
    .then(response => response.json())
    .then(data => {
    document.getElementById('loading-animation').style.display = 'none';
    document.getElementById('ai-img').style.display = 'block';

    //기존 내용에 자동완성 된 내용 더함
    let currentContent = tinyMCE.activeEditor.getContent();
    data.message = data.message.replace(/\n/g, '<br>');
    tinyMCE.activeEditor.setContent(currentContent + data.message);
    })
    .catch(error => {
    console.error('Error:', error);
    document.getElementById('loading-animation').style.display = 'none';
    });
});
});