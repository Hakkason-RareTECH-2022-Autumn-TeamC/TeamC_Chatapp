const btn = document.getElementById('btn');

btn.addEventListener('click', function() {
    const result = confirm('本当に削除しますか？');
    
    if( result ) {
        console.log('OKがクリックされました');
    }
    else {
        console.log('キャンセルがクリックされました');
    }
})
