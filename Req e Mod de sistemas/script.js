
let saldo = 1000.0;
let transacoes = [];

function atualizarTela() {
    
    document.getElementById('saldo').innerText = saldo.toLocaleString('pt-br', { style: 'currency', currency: 'BRL' });
    
 
    const lista = document.getElementById('historico');
    lista.innerHTML = "";
    
    transacoes.forEach(t => {
        const item = document.createElement('li');
        item.textContent = `${t.tipo}: ${t.valor.toLocaleString('pt-br', { style: 'currency', currency: 'BRL' })}`;
        item.style.color = t.tipo === "Saque" ? "#e74c3c" : "#3498db";
        lista.appendChild(item);
    });
}

function depositar() {
    const input = document.getElementById('valor');
    const valor = parseFloat(input.value);

    if (valor > 0) {
        saldo += valor;
        transacoes.unshift({ tipo: "Depósito", valor: valor });
        input.value = "";
        atualizarTela();
    } else {
        alert("Digite um valor válido para depósito.");
    }
}

function sacar() {
    const input = document.getElementById('valor');
    const valor = parseFloat(input.value);

    if (valor > 0 && valor <= saldo) {
        saldo -= valor;
        transacoes.unshift({ tipo: "Saque", valor: valor });
        input.value = "";
        atualizarTela();
    } else {
        alert("Saldo insuficiente ou valor inválido.");
    }
}