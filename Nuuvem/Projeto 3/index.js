const express = require("express")
const app = express()

app.get("/consulta/:id", (req, res) => {
    var cpf = req.query["cpf"];

    res.send("retorno consulta: cpf = " + cpf);
})

app.listen(4000,function(erro){
    if (erro) {
        console.error("Erro ao iniciar o servidor:", erro);
    }else{
        console.log("Servidor iniciado na porta 4000");
    }
})