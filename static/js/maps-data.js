// 5151 Foobar Drive, Bazland, MG

function addressToCoord(address) {
    const addressData = address.trim().split(" ");
    
    const a = {
        number: addressData[0],
        route: addressData[1],
        endPiece: addressData[2],
        city: addressData[3],
        state: addressData[4]
    }

    const url = `https://maps.googleapis.com/maps/api/geocode/json?address=${a[number]}+${a[route]}+${a[endPiece]},+${city},+${state}&key=AIzaSyBfWXO73jO-pX1d0XessOQ9U7del4QY_iQ`

    const req = new XMLHttpRequest();

    req.onreadystatechange = (res) => {
        return res.text;
    }

    req.open("GET", url);
    req.send();
}