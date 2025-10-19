<template>
  <header class="header">
    <div class="header-content">
      <a href="#" class="logo">OrientAI</a>
      <div class="header-actions">
        <a href="#" class="btn-login" @click="$emit('ir-para-home')">Home</a>
        <a href="#" class="btn btn-primary" @click="$emit('iniciar-questionario')">Começar agora</a>
      </div>
    </div>
  </header>
</template>

<script>
import '../styles/header.css'

export default {
  name: 'Header',
  emits: ['iniciar-questionario', 'ir-para-home']
}
</script>
