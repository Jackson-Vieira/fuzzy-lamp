let apiURL = 'http://127.0.0.1:8000/api/';

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const getAllLinks= async () => {
    url = `${apiURL}links/`;
    res = await fetch(url);
    data = await res.json();
    console.log(data);
} 

const getLinkData = async (id) => {
    url = `${apiURL}links/${id}/`;
    try {
        res = await fetch(url);
        data = await res.json();
        console.log(data);
    } catch (error) {
        alert(error);
    }
}

const postLink = async (form) => {
    formData = new FormData(form);
    url = `${apiURL}links/`;
    try {
        res = await fetch(url, {
            method: 'POST',
            body: new FormData(form),
            headers: {'X-CSRFToken': csrftoken},
        });
        data = await res.json();
        form.reset();

    } catch (error) {
        alert(error);
    }
}

const searchLinks = async() => {
    url = `${apiURL}links/`;
    // query_params = new URLSearchParams()
    
}