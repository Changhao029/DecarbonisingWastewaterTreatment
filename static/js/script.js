const normalBackgroundColor = "#182344";
const activeBackgroundColor = "#53baff";

const navbarItems = [
    "Data Report",
    "Data Center",
    "Sharing",
]

const changeElementBackgroundColor = (elementId, color) => {
    document.getElementById(elementId).style.backgroundColor = color;
}

const switchToNavbarItem = (navItem) => {
    navbarItems.forEach((item) => {
        item === navItem ? changeElementBackgroundColor(item, activeBackgroundColor) :
            changeElementBackgroundColor(item, normalBackgroundColor);
    })

    /* Handle any backend loading here */
}