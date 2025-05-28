let use_pos1 = 0;
let use_pos2 = 0;
let Plives = 3;
let Elives = 3;
let background = new Rectangle(100,100);
background.setColor("black");
background.setPosition(0,0);
add(background);
for (let i = 0; i < Plives; i++) {
    use_pos1 = readInt("Give your x position: ");
    use_pos2 = readInt("Give your y position: ");
    let enemypos11 = Math.floor(Math.random() * 101);
    let enemypos12 = Math.floor(Math.random() * 101);
    let enemypos21 = Math.floor(Math.random() * 101);
    let enemypos22 = Math.floor(Math.random() * 101);
    let enemypos31 = Math.floor(Math.random() * 101);
    let enemypos32 = Math.floor(Math.random() * 101);
    let enemy1 = new Rectangle(10, 10);
    enemy1.setColor("red")
    enemy1.setPosition(enemypos11, enemypos12);
    add(enemy1)
    let enemy2 = new Rectangle(10, 10);
    enemy2.setColor("red")
    enemy2.setPosition(enemypos21, enemypos22);
    add(enemy2)
    let enemy3 = new Rectangle(10, 10);
    enemy3.setColor("red")
    enemy3.setPosition(enemypos31, enemypos32);
    add(enemy3)
    let player = new Rectangle(10, 10);
    player.setColor("green");
    player.setPosition(use_pos1, use_pos2);
    add(player);
    let Eattack11 = Math.floor(Math.random() * 101);
    let Eattack12 = Math.floor(Math.random() * 101);
    let Eattack21 = Math.floor(Math.random() * 101);
    let Eattack22 = Math.floor(Math.random() * 101);
    let Eattack31 = Math.floor(Math.random() * 101);
    let Eattack32 = Math.floor(Math.random() * 101);
    if (Eattack11 == use_pos1 || Eattack12 == use_pos2) {
        Plives -= 1;
    }
    if (Eattack21 == use_pos1 || Eattack22 == use_pos2) {
        Plives -= 1;
    }
    if (Eattack31 == use_pos1 || Eattack32 == use_pos2) {
        Plives -= 1;
    }
    if (Plives == 0){
        console.log("You lose.")
    } else if (Elives == 0){
        console.log("You win!")
    }
}
