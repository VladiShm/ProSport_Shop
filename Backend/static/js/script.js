// бургер меню
document.addEventListener("DOMContentLoaded", () => {
  const burger = document.querySelector(".burger");
  const nav = document.querySelector(".nav-links");

  if (burger && nav) {
    burger.addEventListener("click", () => {
      nav.classList.toggle("show");
      burger.classList.toggle("toggle");
    });
  } else {
    console.error("Burger menu or navigation links not found in the DOM.");
  }
});

//итоговая стоимость

    document.addEventListener('DOMContentLoaded', function() {
        var productSelect = document.getElementById('product-select');
        var quantityInput = document.getElementById('id_quantity');
        var totalPriceContainer = document.getElementById('total-price');

        // Функция для обновления общей стоимости
        function updateTotalPrice() {
            var productPrice = parseFloat(productSelect.options[productSelect.selectedIndex].getAttribute('data-price'));
            var quantity = parseInt(quantityInput.value);
            var totalPrice = productPrice * quantity;
            totalPriceContainer.textContent = totalPrice.toFixed(2); // Округление до двух знаков после запятой
        }

        // Обновление общей стоимости при изменении товара или количества
        productSelect.addEventListener('change', updateTotalPrice);
        quantityInput.addEventListener('input', updateTotalPrice);

        // Инициализация общей стоимости при загрузке страницы
        updateTotalPrice();
    });


//текущее время
document.addEventListener("DOMContentLoaded", (event) => {
  function updateClock() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, "0");
    const minutes = String(now.getMinutes()).padStart(2, "0");
    const seconds = String(now.getSeconds()).padStart(2, "0");
    const timeString = `${hours}:${minutes}:${seconds}`;
    document.querySelector(".clock").textContent = timeString;
  }

  setInterval(updateClock, 1000);
  updateClock();
});

//карта
function initMap() {
  const location = { lat: 58.0105, lng: 56.2294 }; // Example coordinates for Perm, Russia
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: location,
  });
  const marker = new google.maps.Marker({
    position: location,
    map: map,
  });
}

// Скрипт даты
function updateDate() {
  const now = new Date();
  const days = [
    "Воскресенье",
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
  ];
  const months = [
    "Январь",
    "Февраль",
    "Март",
    "Апрель",
    "Май",
    "Июнь",
    "Июль",
    "Август",
    "Сентябрь",
    "Октябрь",
    "Ноябрь",
    "Декабрь",
  ];

  const day = days[now.getDay()];
  const date = now.getDate();
  const month = months[now.getMonth()];
  const year = now.getFullYear();

  const dateString = `${day}, ${date} ${month} ${year}`;
  document.querySelector(".date").textContent = dateString;
}

updateDate();

//проверка имени и фамилии
const form = document.querySelector(".forms");
const firstNameInput = document.getElementById("id_first_name");
const lastNameInput = document.getElementById("id_last_name");

form.addEventListener("submit", function (event) {
  const namePattern = /^[а-яА-ЯёЁ]+$/;

  if (!namePattern.test(firstNameInput.value)) {
    alert("Пожалуйста, введите корректное имя (только русские буквы)");
    event.preventDefault();
  }

  if (!namePattern.test(lastNameInput.value)) {
    alert("Пожалуйста, введите корректную фамилию (только русские буквы)");
    event.preventDefault();
  }
});

document.querySelector(".burger-menu").addEventListener("click", function () {
  document.querySelector(".nav-links").classList.toggle("active");
});
