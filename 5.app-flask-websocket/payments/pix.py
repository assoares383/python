import uuid

class Pix:
    def __init__(self):
        pass
    def create_payment(self):
        # criar o pagamento na instituicao financeira
        bank_payment_id = uuid.uuid4()

        hash_payment = f"hash_payment_{bank_payment_id}"

        # gerar o qrcode
        img = qrcode.make(hash_payment)

        # salvar a imagem como arquivo PNG
        img.save(f"static/img/qrcode_payment_{bank_payment_id}.png")

        return {
            "bank_payment_id": bank_payment_id ,
            "qrcode_path": f"qrcode_payment_{bank_payment_id}"
        }