const express = require("express"); //importa o módulo express neste arquivo
const app = express(); //iniciando o express

app.get("/",function(req,res){
    res.send("Bem-vindo ao servidor!");
});

app.listen(4000,function(erro){ // cria a aplicação na porta 4000
    if (erro){
        console.log("Erro ao Iniciar.");
    }else{
        console.log("Servidor Iniciado.");
    }
})