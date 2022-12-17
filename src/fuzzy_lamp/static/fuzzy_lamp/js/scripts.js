const getLinks = async (url) => {
    res = await fetch(url);
    data = await res.json()
    console.log(data);
} 