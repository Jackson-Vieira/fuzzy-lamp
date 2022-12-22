let apiURL = 'http://127.0.0.1:8000/api/';
let url = new URL(getCurrentURL())
let search_params = url.searchParams;
let keyword = search_params.get('name');

function getCurrentURL () {
    return window.location.href
  }

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

const getAllLinks = async (keyword) => {
    let url = `${apiURL}links/`;
    if (keyword) {
        url += `?name=${keyword}`
    }

    try {
        const res = await fetch(url);
        const data = await res.json();
        updateListLinks(data)

    } catch (error) {
        alert(error)
    }
} 

getAllLinks()

const getLinkData = async (id) => {
    const url = `${apiURL}links/${id}/`;
    try {
        res = await fetch(url);
        data = await res.json();
        console.log(data);
    } catch (error) {
        alert(error);
    }
}

const postLink = async (form) => {
    // let formData = new FormData(form);
    const url = `${apiURL}links/`;
    try {
        res = await fetch(url, {
            method: 'POST',
            body: new FormData(form),
            headers: {'X-CSRFToken': csrftoken},
        });
        data = await res.json();
        console.log(data)
        addLink(data); 
        form.reset();

    } catch (error) {
        alert(error);
    }
    alert('a')
    document.getElementById("btn-link-submit").disabled = false;
}

const searchLinks = async(keyword) => {
    if(keyword){
        // const nextState = { additionalInformation: 'Updated the URL with JS' };
        search_params.set('name', keyword)
        url.search = search_params.toString()
        // window.history.pushState(nextState, nextTitle, nextURL);
        window.location.replace(url)
    } 
    // query_params = new URLSearchParams()
}

const updateListLinks = (links) => {
    const listCards = document.querySelector('.list-cards');
    
    links.map( (link) => {
        let template = `
        <div class="card-book">
                <img id="imageCardBook" src="${link.image_url}" alt="">
                <div id="card-info">
                    <h2 id="cardTitle"> <a href=${link.link} >${link.name.length > 30 ? link.name.slice(0, 30)+'  ...' : link.name}</a></h2> 
                    <p> Curent price: R$ ${link.current_price} </p>
                    <p> Last Price: R$ ${link.old_price} </p>
                    <p> Difference: R$ ${link.price_difference} </p>
                    <p id="last-updated"> Updated  ${new Date(Date.parse(link.updated))}</p>
                </div>
        </div>
    `;
        listCards.insertAdjacentHTML("afterbegin", template)
        }
    )
} 

const addLink = (link) => {
    const listCards = document.querySelector('.list-cards');
    let template = `
        <div class="card-book">
                <img id="imageCardBook" src="${link.image_url}" alt="">
                <div id="card-info">
                    <h2 id="cardTitle"> ${link.name.length > 30 ? link.name.slice(0, 30)+' ...' : link.name} <span>
                        (Capa Comum)
                    </span></h2> 
                    <p> Curent price: R$ ${link.current_price} </p>
                    <p> Last Price: R$ ${link.old_price} </p>
                    <p> Difference: R$ ${link.price_difference} </p>
                    <p id="last-updated"> Updated  ${new Date(Date.parse(link.updated))}</p>
                </div>
        </div>
    `;

    listCards.insertAdjacentHTML("afterbegin", template)
}

if (keyword){
    document.getElementById('searchTerm').value = search_params.get('name')
    getAllLinks(keyword)
}



