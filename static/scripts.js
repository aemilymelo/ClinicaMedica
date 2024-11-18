// Função para confirmar a exclusão do paciente
function confirmarExclusao(event) {
    // Impede o envio do formulário se o usuário não confirmar a ação
    if (!confirm('Tem certeza que deseja deletar este paciente?')) {
        event.preventDefault();
    }
}

// Adiciona o evento de confirmação ao botão de exclusão
document.querySelectorAll('form').forEach(function(form) {
    form.addEventListener('submit', confirmarExclusao);
});
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/static/service-worker.js')
        .then((registration) => {
          console.log('Service Worker registrado com sucesso:', registration);
        })
        .catch((error) => {
          console.log('Falha no registro do Service Worker:', error);
        });
    });
  }
  