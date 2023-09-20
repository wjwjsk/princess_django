
    tinymce.init({
        selector: '#content',
    });

    document.querySelector("#image_input").addEventListener('change', function() {
        getBase64(this.files[0]).then(function (base64){
            tinyMCE.activeEditor.insertContent(`<img src="${base64}"/>`);
        });
    });

    function getBase64(file) {
        return new Promise(function(resolve, reject) {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => {
                resolve(reader.result);
            }
            reader.onerror = function (error) {
                reject(error);
            };
        });
    }

    const createDom = (tag,option) => {
        const element = document.createElement('input')
        for (const [key, value] of Object.entries(option)) {
            element.setAttribute(key,value);
        }
        return element
    }
