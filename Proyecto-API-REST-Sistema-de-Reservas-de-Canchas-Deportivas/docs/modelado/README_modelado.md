# Modelado del Dominio - Sistema de Reservas de Canchas Deportivas

## 🎯 Dominio del Sistema
Este sistema permite la gestión integral de reservas para canchas deportivas, facilitando a los usuarios:
- Búsqueda y reserva de canchas disponibles
- Adición de servicios adicionales (alquiler de equipo, entrenador, etc.)
- Gestión de pagos y estados de reserva
- Administración de horarios y disponibilidad

## 🏗️ Decisiones Clave del Modelado

### 1. Entidades Principales
- **User**: Representa usuarios del sistema (clientes y administradores)
- **Court**: Cancha deportiva disponible para reserva
- **Booking**: Reserva principal que relaciona usuario, cancha y servicios
- **Service**: Servicios adicionales disponibles (entidad para relación N-N)
- **BookingService**: Entidad puente para relación N-N entre Booking y Service
- **Schedule**: Horarios específicos de disponibilidad de canchas

### 2. Relaciones Implementadas
- **1-N**: User → Bookings (un usuario muchas reservas)
- **1-N**: Court → Bookings (una cancha muchas reservas)
- **N-N**: Booking ↔ Service (muchos servicios en muchas reservas)
  - **BookingService** es la entidad puente con atributos adicionales
- **1-N**: Court → Schedules (una cancha muchos horarios)

### 3. Reglas de Integridad
- **UNIQUE**: Email de usuario (no se permiten duplicados)
- **NOT NULL**: Campos obligatorios en todas las entidades
- **CHECK**: Validación de fechas (end_time > start_time)
- **FOREIGN KEYS**: Todas las relaciones con integridad referencial
- **TIMESTAMPS**: created_at y updated_at en todas las entidades

### 4. Normalización
- Separación de servicios en entidad independiente
- Entidad puente para relación N-N con atributos propios
- Evitar datos duplicados mediante relaciones

## 📋 Supuestos del Modelo

### Supuestos de Negocio
1. Las reservas tienen una duración mínima de 1 hora
2. Los servicios adicionales son opcionales
3. Los usuarios deben estar registrados para reservar
4. Las canchas tienen disponibilidad por horarios específicos
5. Los precios de servicios pueden variar independientemente

### Supuestos Técnicos
1. Base de datos PostgreSQL con soporte para tipos ENUM
2. Huso horario configurado para toda la aplicación
3. Validación de solapamiento de horarios a nivel de aplicación
4. Sistema de autenticación basado en email/password

## 🔧 Cumplimiento de Requisitos

### ✅ Requisitos Mínimos Cumplidos
1. **5+ entidades**: User, Court, Booking, Service, BookingService, Schedule (6 entidades)
2. **Entidad Usuario**: User con sistema de autenticación
3. **Entidad principal**: Booking como núcleo del negocio
4. **Entidad de detalle**: BookingService como entidad puente
5. **Timestamps**: created_at, updated_at en todas las entidades
6. **Relación 1-N**: User → Bookings, Court → Bookings
7. **Relación N-N**: Booking ↔ Service (con BookingService como puente)
8. **Regla de integridad**: Email único en User

### ✅ Implementación ORM
- Modelos SQLAlchemy con relaciones bidireccionales
- Constraints a nivel de base de datos
- Migraciones con Alembic
- Enums para tipos predefinidos
- Métodos de negocio en los modelos

## 🚀 Próximos Pasos
1. Implementar sistema de pagos
2. Añadir sistema de calificaciones
3. Implementar notificaciones por email
4. Añadir reportes y estadísticas
5. Integración con APIs de pago externas
