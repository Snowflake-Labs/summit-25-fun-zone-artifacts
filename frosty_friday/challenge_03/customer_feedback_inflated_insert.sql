create or replace schema mikedroog.challenge_003_setup;

CREATE OR REPLACE TABLE customer_feedback_en_inflated (
  review_id INT,
  review_text STRING
);
INSERT INTO customer_feedback_en_inflated (review_id, review_text) VALUES
(1, 'It was okay, but could be better. Excellent customer support throughout the process. It was okay, but could be better. Excellent customer support throughout the process. It was okay, but could be better. Excellent customer support throughout the process. It was okay, but could be better. Excellent customer support throughout the process. It was okay, but could be better. Excellent customer support throughout the process.');

CREATE OR REPLACE TABLE customer_feedback_es_inflated (
  review_id INT,
  review_text STRING
);
INSERT INTO customer_feedback_es_inflated (review_id, review_text) VALUES
(1, 'Estuvo bien, pero podría mejorar. No estoy satisfecho con la calidad del artículo. Estuvo bien, pero podría mejorar. No estoy satisfecho con la calidad del artículo. Estuvo bien, pero podría mejorar. No estoy satisfecho con la calidad del artículo. Estuvo bien, pero podría mejorar. No estoy satisfecho con la calidad del artículo. Estuvo bien, pero podría mejorar. No estoy satisfecho con la calidad del artículo.');

CREATE OR REPLACE TABLE customer_feedback_fr_inflated (
  review_id INT,
  review_text STRING
);
INSERT INTO customer_feedback_fr_inflated (review_id, review_text) VALUES
(1, 'Je recommanderais certainement ce produit. La livraison était rapide et le service excellent. Je recommanderais certainement ce produit. La livraison était rapide et le service excellent. Je recommanderais certainement ce produit. La livraison était rapide et le service excellent. Je recommanderais certainement ce produit. La livraison était rapide et le service excellent. Je recommanderais certainement ce produit. La livraison était rapide et le service excellent.');

CREATE OR REPLACE TABLE customer_feedback_de_inflated (
  review_id INT,
  review_text STRING
);
INSERT INTO customer_feedback_de_inflated (review_id, review_text) VALUES
(1, 'Ich würde dieses Produkt auf jeden Fall empfehlen. Es war okay, aber es könnte besser sein. Ich würde dieses Produkt auf jeden Fall empfehlen. Es war okay, aber es könnte besser sein. Ich würde dieses Produkt auf jeden Fall empfehlen. Es war okay, aber es könnte besser sein. Ich würde dieses Produkt auf jeden Fall empfehlen. Es war okay, aber es könnte besser sein. Ich würde dieses Produkt auf jeden Fall empfehlen. Es war okay, aber es könnte besser sein.');

CREATE OR REPLACE TABLE customer_feedback_ja_inflated (
  review_id INT,
  review_text STRING
);
INSERT INTO customer_feedback_ja_inflated (review_id, review_text) VALUES
(1, '全体的に優れたカスタマーサポートでした。 この製品は間違いなくおすすめです。 全体的に優れたカスタマーサポートでした。 この製品は間違いなくおすすめです。 全体的に優れたカスタマーサポートでした。 この製品は間違いなくおすすめです。 全体的に優れたカスタマーサポートでした。 この製品は間違いなくおすすめです。 全体的に優れたカスタマーサポートでした。 この製品は間違いなくおすすめです。');