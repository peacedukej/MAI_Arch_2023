workspace {
    name "Мессенджер-приложение"
    description "Система обмена сообщениями с поддержкой пользователей, групповых и PtP чатов."

    # Включаем режим с иерархической системой идентификаторов
    !identifiers hierarchical

    #!docs documentation
    #!adrs decisions

    model {
        # Описание компонент модели
        user = person "Пользователь мессенджера"
        group_chat = softwareSystem "Групповой чат"
        ptp_chat = softwareSystem "PtP Чат"

        messenger_app = softwareSystem "Мессенджер-приложение" {
            description "Система обмена сообщениями"

            user_service = container "User service" {
                description "Сервис управления пользователями"
            }

            chat_service = container "Chat service" {
                description "Сервис управления чатами"
            }

            message_service = container "Message service" {
                description "Сервис управления сообщениями"
            }

            database = container "База данных" {
                description "Хранение данных"
                technology "MongoDB"
                tags "database"
            }

            user -> user_service "Использует"
            user -> chat_service "Использует"
            user -> message_service "Использует"

            group_chat -> chat_service "Использует"
            group_chat -> message_service "Использует"

            ptp_chat -> chat_service "Использует"
            ptp_chat -> message_service "Использует"


            user_service -> database "Чтение и запись"
            chat_service -> database "Чтение и запись"
            chat_service -> message_service "Использует"
            message_service -> database "Чтение и запись"
        }

        user -> messenger_app "Использует мессенджер"
        group_chat -> messenger_app "Использует мессенджер"
        ptp_chat -> messenger_app "Использует мессенджер"

        deploymentEnvironment "Production" {
            deploymentNode "Messenger Server" {
                containerInstance messenger_app.user_service
                containerInstance messenger_app.chat_service
                containerInstance messenger_app.message_service
            }

            deploymentNode "Database Server" {
                containerInstance messenger_app.database
            }
        }
    }

    views {
        themes default

        properties {
            structurizr.tooltips true
        }

        !script groovy {
            workspace.views.createDefaultViews()
            workspace.views.views.findAll { it instanceof com.structurizr.view.ModelView }.each { it.enableAutomaticLayout() }
        }

        dynamic messenger_app "ContextDiagram" {
            autoLayout
            user -> messenger_app.user_service "Регистрация нового пользователя"
            user -> messenger_app.chat_service "Создание группового чата"
            user -> messenger_app.message_service "Отправка PtP сообщения"
            group_chat -> messenger_app.chat_service "Добавление пользователя в чат"
            group_chat -> messenger_app.message_service "Добавление сообщения в групповой чат"
            group_chat -> messenger_app.message_service "Загрузка сообщений группового чата"


            ptp_chat -> messenger_app.message_service "Отправка PtP сообщения"
            ptp_chat -> messenger_app.message_service "Получение PtP списка сообщений"
        }

        container messenger_app "ContainerDiagram" {
            include *
            autolayout lr
        }

        deployment messenger_app Production {
            include *
            autolayout lr
        }

        dynamic messenger_app "SendingMessageToGroupChat" {
            autoLayout
            user -> messenger_app.chat_service "Отправить сообщение"
            messenger_app.chat_service -> messenger_app.message_service "Обработать сообщение"
            messenger_app.message_service -> messenger_app.database "Сохранить сообщение"
        }

        dynamic messenger_app "SendingPtPMessage" {
            autoLayout
            user -> messenger_app.message_service "Отправить PtP сообщение"
            messenger_app.message_service -> messenger_app.database "Сохранить PtP сообщение"
        }

        dynamic messenger_app "LoadingGroupChatMessages" {
            autoLayout
            user -> messenger_app.chat_service "Запросить сообщения"
            messenger_app.chat_service -> messenger_app.message_service "Получить сообщения"
            messenger_app.message_service -> messenger_app.database "Загрузить сообщения"
        }

        dynamic messenger_app "GettingPtPListMessages" {
            autoLayout
            user -> messenger_app.message_service "Запросить список сообщений"
            messenger_app.message_service -> messenger_app.database "Получить список сообщений"
        }

        styles {
            element "database" {
                shape cylinder
            }
        }
    }
}
