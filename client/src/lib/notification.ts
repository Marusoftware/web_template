import { writable } from "svelte/store"

interface Notification {
    id?:number,
    kind:"info"|"warn",
    title:string,
    subtitle?: string,
    caption?: string,
    timeout?: number
}

export const notifications=writable<Notification[]>([])

export function showNotification(notification:Notification){
    const defaults={
        id :Math.floor(Math.random() * 10000),
        subtitle: "",
        caption: "",
        timeout:5
    }
    notification={
        ...defaults,
        ...notification
    }
    if(notification.timeout!==0){
        setTimeout(() => {
            destroyNotification(notification.id??0) // dummy
        }, (notification.timeout??0)*1000);
    }
    notifications.update((all) =>[notification, ...all])
    return notification.id
}

export const destroyNotification = (id:number) => {
    notifications.update((all) => all.filter((t) => t.id !== id))
}
