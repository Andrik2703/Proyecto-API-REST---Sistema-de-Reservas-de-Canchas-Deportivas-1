# Modelado del Dominio - Sistema de Reservas de Canchas Deportivas

## 🎯 Dominio del Sistema

El sistema resuelve la gestión integral de reservas para canchas deportivas, permitiendo a los usuarios:
- Buscar y reservar canchas disponibles según deporte y horario
- Gestionar pagos y confirmaciones de reservas
- Administrar equipos adicionales (pelotas, bebidas, etc.)
- Controlar la disponibilidad de canchas mediante horarios predefinidos

## 🏗️ Decisiones Clave del Modelado

### 1. Estructura de Entidades
- **Usuario**: Centraliza todas las operaciones del cliente
- **Cancha (Field)**: Entidad principal del negocio con atributos específicos por deporte
- **Reserva**: Gestiona el ciclo de vida completo de una reserva
- **Items de Reserva**: Permite agregar productos/servicios adicionales (relación 1:N)
- **Pago**: Separa la lógica financiera de la reserva
- **Horario (Schedule)**: Controla disponibilidad por día y hora

### 2. Relaciones Implementadas
- **1:N**: Usuario → Reservas (un usuario muchas reservas)
- **1:N**: Cancha → Reservas (una cancha muchas reservas)
- **1:N**: Reserva → Items (una reserva muchos items)
- **N:N Implícita**: Usuario ↔ Cancha (a través de Reservas)
- **1:1**: Reserva → Pago (cada reserva tiene un pago asociado)

### 3. Reglas de Integridad
- Email único por usuario
- Transaction_id único por pago
- Precios positivos en todos los modelos
- Rangos de tiempo válidos (end_time > start_time)
- Cantidades positivas en items

### 4. Normalización
- Separación de preocupaciones: reservas, pagos, items
- Tabla Schedule para horarios reutilizables
- Enums para estados consistentes (ReservationStatus, PaymentStatus)

## 📝 Supuestos (Assumptions)

### Supuestos de Negocio
1. Las reservas se cobran por hora completa
2. Los precios de canchas son fijos por hora
3. Los items adicionales tienen precios unitarios
4. Un pago corresponde a una sola reserva
5. Los horarios de canchas se definen por día de semana

### Supuestos Técnicos
1. Sistema multi-usuario con roles (cliente, admin, manager)
2. Base de datos relacional (PostgreSQL/MySQL/SQLite)
3. API RESTful para frontend/móvil
4. Autenticación basada en tokens JWT
5. Zona horaria UTC para consistencia

## 🔧 Validaciones Implementadas

### Validaciones de Dominio
1. **Usuario**: Email válido, contraseña encriptada
2. **Reserva**: No superposición de horarios, estado válido
3. **Pago**: Monto positivo, estado válido
4. **Cancha**: Precio positivo, capacidad positiva
5. **Items**: Cantidad positiva, precio positivo

### Validaciones Temporales
- `created_at`: Fecha de creación automática
- `updated_at`: Actualización automática al modificar
- `payment_date`: Fecha del pago procesado

## 🚀 Consideraciones para Extensión

### Escalabilidad
1. Agregar tabla `Promotions` para descuentos
2. Tabla `Reviews` para calificaciones de canchas
3. `Notification` para recordatorios de reservas
4. `Team` para reservas grupales

### Rendimiento
- Índices en campos de búsqueda frecuente
- Caché de disponibilidad de canchas
- Paginación en listados grandes

## 📊 Requisitos Mínimos Cumplidos

✅ **5+ Entidades**: User, Field, Reservation, ReservationItem, Payment, Schedule  
✅ **Entidad Usuario**: User con autenticación y roles  
✅ **Entidad Principal**: Field (cancha deportiva)  
✅ **Entidad de Detalle**: ReservationItem (items adicionales)  
✅ **Timestamps**: created_at, updated_at en todas las entidades  
✅ **Relación 1:N**: User → Reservations  
✅ **Relación N:N**: User ↔ Field (a través de Reservation)  
✅ **Reglas de Integridad**: Unique constraints, check constraints, not null
