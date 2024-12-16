// Fungsi untuk menampilkan atau menyembunyikan dropdown menu
function toggleDropdown(event) {
    event.preventDefault(); // Mencegah tautan default
    const dropdownMenu = event.target.nextElementSibling; // Ambil elemen berikutnya (menu)
    dropdownMenu.style.display = dropdownMenu.style.display === "block" ? "none" : "block";
}

// Tutup dropdown saat mengklik di luar
document.addEventListener("click", (event) => {
    const dropdowns = document.querySelectorAll(".dropdown-menu");
    dropdowns.forEach((menu) => {
        if (!menu.contains(event.target) && !menu.previousElementSibling.contains(event.target)) {
            menu.style.display = "none";
        }
    });
});