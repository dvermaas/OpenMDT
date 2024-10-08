function showModal(modalTitle, modalBody) {
    const modal = document.getElementById('Modal');
    modal.querySelector('.modal-title').textContent = modalTitle;
    modal.querySelector('.modal-body').innerHTML = modalBody;
    const modalInstance = new bootstrap.Modal(modal);
    modalInstance.show();
}

function getHeight() {
    const navbarHeight = 40
    const mt4Height = 24;
    const availableHeight = window.innerHeight - navbarHeight - (mt4Height * 2);
    console.log(availableHeight);
}