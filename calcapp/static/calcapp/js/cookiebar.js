document.addEventListener('DOMContentLoaded', function() {
            const cookieNotice = document.querySelector('.cookie-notice');
            const acceptButton = cookieNotice.querySelector('button');

            // Проверяем, есть ли cookie о согласии
            if (!document.cookie.includes('cookie_consent=true')) {
                cookieNotice.style.display = 'block';
            }

            // Обработчик кнопки «Понятно»
            acceptButton.addEventListener('click', function() {
                // 1. Отправляем запрос на бэкенд (если используется вариант 3)
                fetch('/accept-cookie/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]')?.value
                    },
                    body: JSON.stringify({
                        session_key: document.getElementById('session-key').value
                    })
                })
                .then(() => {
                    // 2. Устанавливаем cookie на фронте
                    const date = new Date();
                    date.setFullYear(date.getFullYear() + 1);
                    document.cookie = `cookie_consent=true; expires=${date.toUTCString()}; path=/; SameSite=Lax`;

                    // 3. Скрываем баннер
                    cookieNotice.style.display = 'none';
                });
            });
        });