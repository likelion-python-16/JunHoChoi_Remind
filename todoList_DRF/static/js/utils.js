
function datetimeToString(datetime) {
    if (!datetime) return '';
    const date = new Date(datetime);
    return date.toLocaleString(); // "2025.6.19 오후 9:12:34" 등으로 출력
}

