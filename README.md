# 🎬 iCinema - Sistema de Gerenciamento de Cinema

Bem-vindo ao **iCinema**, um sistema de gerenciamento de cinema desenvolvido para facilitar a compra de ingressos, avaliação de filmes e muito mais! Este projeto simula a experiência de um cinema, permitindo que os usuários escolham filmes, horários, assentos e métodos de pagamento, além de avaliar os filmes assistidos.

---

## 📌 Requisitos

- **Python 3.x** instalado.
- Bibliotecas necessárias: `qrcode` e `smtplib` (para envio de e-mails).
- Um arquivo `users.json` para armazenar os dados dos usuários (será criado automaticamente se não existir).

---

## 🎥 Funcionalidades

•Cinema and Movie Listings: Displaying listings of cinemas and movies;✅
• Seat Selection and Booking: Enabling users to select seats and book tickets;✅
• Payment Processing: Secure processing of ticket payments;✅
• User Account Management: Creating and managing user profiles;✅
• Booking History and Cancellations: Viewing past bookings and managing cancellations;✅
• Promotions and Discounts: Offering and managing discounts and special offers;✅
• Real-Time Seat Availability: Showing real-time availability of seats in cinemas;✅
• Mobile Ticketing: Generating mobile tickets for ease of access;✅ (gera o ingresso e envia por email)
• Customer Reviews and Ratings: Feature for users to rate and review movies;✅
• Notification and Alerts: Sending notifications for new releases and booking confirmations.✅ ( apenas confirmação da reserva por email)

### 1️⃣ Criação de Conta e Login
- **Criar conta**: Insira seu nome, e-mail e senha para criar uma conta.
- **Login**: Faça login com seu e-mail e senha para acessar o sistema.

### 2️⃣ Compra de Ingressos
- Escolha entre os cinemas disponíveis: **Centerplex, Cinesystem ou Kinoplex**.
- Selecione o filme desejado e o horário.
- Escolha seus assentos e finalize a compra.
- **Métodos de pagamento**:
  - 💳 Cartão de Crédito/Débito
  - 💵 Dinheiro
  - 🔄 PIX
- Após a compra, um ingresso com **QR Code** será enviado para o seu e-mail.

### 3️⃣ Avaliação de Filmes
- Após assistir a um filme, você pode deixar uma avaliação e uma nota **(de 0 a 10)**.
- As avaliações são armazenadas e podem ser visualizadas por outros usuários.

### 4️⃣ Histórico de Compras
- Visualize seu histórico de compras, incluindo detalhes como **cinema, filme, assentos, horário e código do ingresso**.
- Cancele reservas (**se permitido pelo tempo limite**).

### 5️⃣ Cupom de Desconto
- Use o cupom **10CONTO** para ganhar **10% de desconto** na compra de ingressos. 🎟️💰

---

## 📦 Classes das Versões Anteriores

### 🔹 **Parte 1**
- **Usuário**: Informações da conta.
- **Reserva**: Escolha de assento e reserva.
- **Cinemas e filmes**: Listagem e exibição de opções.
- **Sistema geral**: Gerenciamento do fluxo do programa.

### 🔹 **Parte 2**
- **`review`**: Responsável pelas avaliações dos filmes.
- **`conta`**: Gerencia as informações dos usuários.
- **`movie`**: Responsável pela seleção de filmes, cadeiras e pagamento.

---

